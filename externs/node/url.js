

/**
 * @type {Object.<string,*>}
 */
var url = {};

/**
 * @typedef {{
 * href: ?string,
 * protocol: ?string,
 * host: ?string,
 * auth: ?string,
 * hostname: ?string,
 * port: ?string,
 * pathname: ?string,
 * search: ?string,
 * path: ?string,
 * query: ?string,
 * hash: ?string
 * }}
 */
var URL;

/**
 * @param {string} urlStr
 * @param {boolean=} parseQueryString
 * @param {boolean=} slashesDenoteHost
 * @return {URL}
 * @nosideeffects
 */
url.parse = function(urlStr, parseQueryString, slashesDenoteHost) {};

/**
 * @param {URL} urlObj
 * @return {string}
 * @nosideeffects
 */
url.format = function(urlObj) {};

/**
 * @param {string} from
 * @param {string} to
 * @return {string}
 * @nosideeffects
 */
url.resolve = function(from, to) {};
