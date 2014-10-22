

/**
 *
 * @namespace
 */
var hbase = {};


/**
 * @constructor
 * @extends {Error}
 */
hbase.Error = function() {

  /**
   * @type {number}
   */
  this.code;

  /**
   * @type {string}
   */
  this.body;
};


/**
 * @constructor
 * @param {{
 *  host:string,
 *  port: number
 * }} options
 */
hbase.Client = function(options) {};


/**
 * @param {string} table
 * @param {string} row
 * @param {number=} opt_timeout
 * @return {!hbase.Row}
 */
hbase.Client.prototype.getRow = function(table, row, opt_timeout) {};


/**
 * @constructor
 * @param {!hbase.Client} client
 * @param {string} table
 * @param {string} row
 */
hbase.Row = function(client, table, row) {};


/**
 * @param {(string|!Array.<string>)} columns
 * @param {(string|!Array.<string>)} values
 * @param {function(hbase.Error)} callback
 * @param {number=} opt_timeout
 */
hbase.Row.prototype.put = function(columns, values, callback, opt_timeout) {};


/**
 * @param {(string|!Array.<string>)} columns
 * @param {function(hbase.Error)} callback
 * @param {number=} opt_timeout
 */
hbase.Row.prototype.delete = function(columns, callback, opt_timeout) {};


/**
 * @param {string} column
 * @param {!Object.<string>} options
 * @param {function(hbase.Error, Array.<{column:string, $:string}>)} callback
 * @param {number=} opt_timeout
 */
hbase.Row.prototype.get = function(column, options, callback, opt_timeout) {};
