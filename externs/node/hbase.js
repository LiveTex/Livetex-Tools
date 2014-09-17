

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
 * @return {!hbase.Row}
 */
hbase.Client.prototype.getRow = function(table, row) {};


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
 */
hbase.Row.prototype.put = function(columns, values, callback) {};


/**
 * @param {(string|!Array.<string>)} columns
 * @param {function(hbase.Error)} callback
 */
hbase.Row.prototype.delete = function(columns, callback) {};


/**
 * @param {string} column
 * @param {!Object.<string>} options
 * @param {function(hbase.Error, Array.<{column:string, $:string}>)} callback
 */
hbase.Row.prototype.get = function(column, options, callback) {};
