
/**
 * @type {Object.<string,*>}
 */
var path = {};

/**
 * @param {string} p
 * @return {string}
 * @nosideeffects
 */
path.normalize = function(p) {};

/**
 * @param {...string} var_args
 * @return {string}
 * @nosideeffects
 */
path.join = function(var_args) {};

/**
 * @param {string} from
 * @param {string=} to
 * @return {string}
 * @nosideeffects
 */
path.resolve = function(from, to) {};

/**
 * @param {string} from
 * @param {string} to
 * @return {string}
 * @nosideeffects
 */
path.relative = function(from, to) {};

/**
 * @param {string} p
 * @return {string}
 * @nosideeffects
 */
path.dirname = function(p) {};

/**
 * @param {string} p
 * @param {string=} ext
 * @return {string}
 * @nosideeffects
 */
path.basename = function(p, ext) {};

/**
 * @param {string} p
 * @return {string}
 * @nosideeffects
 */
path.extname = function(p) {};

/**
 * @type {string}
 */
path.sep;
