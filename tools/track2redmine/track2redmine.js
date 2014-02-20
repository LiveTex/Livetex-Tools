

var https = require('https');
var http = require('http');
var xml2js = require('./xml2js/lib/xml2js.js');


// Util ------------------------------------------------------------------------

/**
 * Decodes special characters in url.
 *
 * @param {string} url URL-string.
 * @return {string} Decoded string.
 */
unescape = function(url) {
  try {
    return decodeURIComponent(url);
  } catch (error) {
    console.error('Malformed url: "' + url + '". [unescape]');
  }

  return '';
};


// Async -----------------------------------------------------------------------


/**
 * @param {!function(*, !Function, function(string, number=))} handler
 * Задача обработки данных.
 * @return {!function(*, !Function, function(string, number=))}
 * Задача генерации и обработки.
 */
each = function (handler) {
  return function(array, complete, cancel) {
    var context = this;

    function createHandler(item) {
      return function(_, localNext, localCancel) {
        handler.call(context, item, localNext, localCancel);
      };
    }

    var items = [].concat(array);
    var i = 0,
        l = items.length;

    var workers = new Array(l);
    while (i < l) {
      workers[i] = createHandler(items[i]);

      i += 1;
    }

    collect(workers).call(context, null, complete, cancel);
  }
};


/**
 * @param {!Array.<!function(*, !Function, function(string, number=))>} tasks
 * Набор задач.
 * @return {!function(*, !Function, function(string, number=))}
 * Задача парралельного исполнения.
 */
collect = function(tasks) {
  return function(data, complete, cancel) {
    var remainingTaskCount = tasks.length;
    var context = this;
    var result = [];

    /**
     * @param {*} localData Данные.
     */
    function localComplete(localData) {
      if (localData !== null) {
        result = result.concat(localData);
      }

      if (remainingTaskCount > 0) {
        remainingTaskCount -= 1;
      } else {
        complete(result);
      }
    }

    var i = 0,
        l = tasks.length;

    while (i < l) {
      tasks[i].call(context, data, localComplete, cancel);

      i += 1;
    }

    localComplete(null);
  };
};


// YouTrack --------------------------------------------------------------------


/**
 * @param {function(Object)} complete Result handler.
 * @param {function(string)} cancel Error handler.
 */
function youTrackLogin(complete, cancel) {

  var data = 'login=root&password=SmetubViaraivHeolCerAmBijnenOgfivBaikyaryonweitjusimkaceujviddUj';

  var options = {
    hostname: 'youtrack.livetex.ru',
    port: 80,
    path: '/rest/user/login',
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
      'Content-Length': data.length,
      'Cookie': ''
    }
  };

  var req = http.request(options, function(res) {
    res.on('data', function() {
      var cookie = ['$Version = 0;'].concat(res.headers['set-cookie']);
      complete(cookie);
    });
  });

  req.on('error', cancel);
  req.write(data);
  req.end();

}


/**
 * @param {!Object} cookie
 * @param {string} project
 * @param {function(Object)} complete Result handler.
 * @param {function(string)} cancel Error handler.
 */
function getYouTrackIssuesCount(cookie, project, complete, cancel) {
  var issues = '';

  var options = {
    hostname: 'youtrack.livetex.ru',
    port: 80,
    path: '/rest/issue/count?filter=project:' + project,
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'Content-Length': 0,
      'Cookie': cookie
    }
  };

  var req = http.request(options, function(res) {

    res.on('data', function(data) {
      issues += data.toString();
    });

    res.on('end', function() {

      var start = issues.indexOf('{');
      var end = issues.lastIndexOf('}');
      var result = JSON.parse(issues.substring(start, end + 1));

      complete(result.value);
    });
  });

  req.on('error', cancel);
  req.end();
}


/**
 * @param {!Object} issue
 * @returns {{id: string, status: string=, sprint: number=, ticket: number=}}
 */
function serializeYouTrackIssueData(issue) {

  var data = {
    'id': issue['$']['id']
  };

  var fields = issue['field'];

  for (var i = 0; i < fields.length; i++) {

    if (fields[i]['$']['name'] === 'State') {
      data['status'] = fields[i]['value'][0];
    }
    if (fields[i]['$']['name'] === 'Redmine') {
      data['ticket'] = Number(fields[i]['value'][0]);
    }
    if (fields[i]['$']['name'] === 'Fix versions') {
      var field = fields[i]['value'][0];
      var start = field.indexOf(' ');

      data['sprint'] = Number(field.substr(start + 1));
    }
  }

  return data;
}


/**
 * @param {Array.<Object>} issues
 * @return {number}
 */
function getSprintNumber(issues) {

  var sprintNumber = 0;

  for (var i = 0; i < issues.length; i++) {
    var number = issues[i]['sprint'];

    if (number > sprintNumber) {
      sprintNumber = number;
    }
  }

  return sprintNumber;
}


/**
 * @param {Array.<Object>} issues
 */
function checkDoubledIssues(issues) {

  var doubledIssues = [];

  for (var i = 0; i < issues.length; i++) {
    var ticket = issues[i]['ticket'];
    var j = 0;
    while (j < issues.length) {
      var issue = issues[j];
      if (j !== i) {
        if (issue['ticket'] === ticket) {
          doubledIssues.push(issue);
        }
      }
      j += 1;
    }
  }

  if (doubledIssues.length) {
    console.log('ERROR: There are some issues with doubled tickets:');
    for (var k = 0; k < doubledIssues.length; k++) {
      console.log(doubledIssues[k]['id'], ':', doubledIssues[k]['ticket']);
    }
    process.exit();
  }
}


/**
 * @param {Array.<Object>} issues
 * @return {Array.<Object>}
 */
function filterYouTrackIssues(issues) {

  var filteredIssues = [];
  var sprintNumber = getSprintNumber(issues);

  for (var i = 0; i < issues.length; i++) {
    var issue = issues[i];

    if ((issue['sprint'] == sprintNumber) &&
        (issue['ticket'] !== undefined) &&
        ((issue['status'] === 'In Progress') ||
            (issue['status'] === 'Ready') ||
            (issue['status'] === 'Done'))) {
      filteredIssues.push(issue);
    }
  }

  checkDoubledIssues(filteredIssues);
  return filteredIssues;
}


/**
 * @param {Array.<Object>} issues
 * @return {Array.<Object>}
 */
function serializeYouTrackIssuesData(issues) {

  var serializedIssues = [];

  for (var i = 0; i < issues.length; i++) {
    serializedIssues.push(serializeYouTrackIssueData(issues[i]));
  }

  return filterYouTrackIssues(serializedIssues);
}

/**
 * @param {string} project.
 * @param {function(Object)} complete Result handler.
 * @param {function(string)} cancel Error handler.
 */
function getYouTrackIssues(project, complete, cancel) {
  youTrackLogin(function(cookie) {
    getYouTrackIssuesCount(cookie, project, function(count) {
      var issues = '';

      var options = {
        hostname: 'youtrack.livetex.ru',
        port: 80,
        path: '/rest/issue?filter=project:' + project + '&with=Redmine' +
            '&with=State&with=Fix+versions&max=' + count.toString(),
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'Content-Length': 0,
          'Cookie': cookie
        }
      };

      var req = http.request(options, function(res) {

        res.on('data', function(data) {
          issues += data.toString();
        });

        res.on('end', function() {
          xml2js.parseString(unescape(issues), function (err, result) {
            if (err) {
              cancel(err);
            } else {
              var issues = result['issueCompacts']['issue'];
              if (issues !== undefined) {
                complete(serializeYouTrackIssuesData(issues));
              }
            }
          });
        });

      });

      req.on('error', cancel);
      req.end();
    }, cancel);
  }, cancel);
}


// Redmine ---------------------------------------------------------------------


/**
 * @param {!Object} issue
 * @return {{id: number, status: !Object}}
 */
function serializeRedmineIssueData(issue) {
  return {
    'id': issue['issue']['id'],
    'status': issue['issue']['status']['name']
  };
}


/**
 * @param {number} ticket
 * @param {function(Object)} complete Result handler.
 * @param {function(string)} cancel Error handler.
 */
function getRedmineIssue(ticket, complete, cancel) {
  var issue = '';
  var options = {
    hostname: 'redmine.livetex.ru',
    port: 443,
    path: '/issues/' + ticket.toString() + '.json',
    method: 'GET',
    headers: {
      'X-Redmine-API-Key': 'aa6afba88ecaea5938ead668af1b53c35365a977',
      'Content-Type': 'application/json'
    }
  };

  var req = https.request(options, function(res) {

    res.on('data', function(data) {
      issue += data.toString();
    });

    res.on('end', function() {
      try {
        complete(serializeRedmineIssueData(JSON.parse(issue)));
      } catch (error) {
        cancel('Hey! Here is some shit!:', error,
            'it seems your ticket', ticket, 'doesn\'t exist! Check up issue');
      }
    })

  });

  req.on('error', cancel);
  req.end();

}


/**
 * @param {number} ticket.
 * @param {Object} data Data to update an issue.
 * @param {function(*)} complete Result handler.
 * @param {function(string)} cancel Error handler.
 */
function updateRedmineIssue(ticket, data, complete, cancel) {

  data = Buffer(JSON.stringify(data));

  var options = {
    hostname: 'redmine.livetex.ru',
    port: 443,
    path: '/issues/' + ticket.toString() + '.json',
    method: 'PUT',
    headers: {
      'X-Redmine-API-Key': 'aa6afba88ecaea5938ead668af1b53c35365a977',
      'Content-Length': data.length,
      'Content-Type': 'application/json'
    }
  };

  var req = https.request(options, function(res) {
    res.on('end', function(data) {
      complete(data);
    });
  });

  req.on('error', cancel);
  req.write(data);
  req.end();
}


/**
 * @param {string} status
 * @param {function(!Object)} complete Result handler.
 * @param {function(string)} cancel Error handler.
 */
function getRedmineStatusObject(status, complete, cancel) {

  var options = {
    hostname: 'redmine.livetex.ru',
    port: 443,
    path: '/issue_statuses.json',
    method: 'GET',
    headers: {
      'X-Redmine-API-Key': 'aa6afba88ecaea5938ead668af1b53c35365a977',
      'Content-Type': 'application/json'
    }
  };

  var req = https.request(options, function(res) {

    res.on('data', function(data) {

      var statuses = JSON.parse(data.toString())['issue_statuses'];

      for (var i = 0; i < statuses.length; i++) {
        var statusObject = statuses[i];
        if (statusObject.name === status) {
          complete({
            'issue': {
              'status_id': statusObject.id
            }
          });
          break;
        }
      }
    });

  });

  req.on('error', cancel);
  req.end();
}


/**
 * @param {string} status
 * @return {string}
 */
function mapStatus(status) {
  var map = {
    'In Progress': 'В работе',
    'Ready': 'Решена',
    'Done': 'Проверено'
  };
  return map[status];
}


/**
 * @param {Object} youTrackIssue
 * @param {function(!Object)} complete Result handler.
 * @param {function(string)} cancel Error handler.
 */
function update(youTrackIssue, complete, cancel) {
  var ticket = youTrackIssue['ticket'];
  getRedmineIssue(ticket, function(redmineIssue) {
    var status = redmineIssue['status'];
    if ((status !== 'Закрыта') &&
        (status !== 'Фидбек') &&
        (status !== 'Отказ')) {
      var correctStatus = mapStatus(youTrackIssue['status']);
      if (status !== correctStatus) {
        console.log('Ticket', ticket,
            'will be updated with status', correctStatus);
        getRedmineStatusObject(correctStatus, function(statusObject) {
          updateRedmineIssue(ticket, statusObject, complete, cancel);
        }, cancel);
      }
    }
  }, function(error) {
    var issueError = 'Houston! We have problems with issue ' +
        youTrackIssue['id'] + ' ERROR: ' + error;
    cancel(issueError);
  })
}

// General ---------------------------------------------------------------------


/**
 *
 * @param {string} project
 * @param {function(!Object)} complete Result handler.
 * @param {function(string)} cancel Error handler.
 */
function synchronize(project, complete, cancel) {
  getYouTrackIssues(project, function(youTrackIssues) {
    each(update).call(this, youTrackIssues, complete, cancel);
  }, cancel);
}


synchronize(process.argv[2], function(data) {
  console.log('OKAY', data);
}, console.error);
