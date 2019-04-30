import queryString from 'qs'
import _ from 'underscore';

export default {
  parse(key = null) {
    const params = queryString.parse(location.search.substring(1));
    return key ? params[key] : params
  },
  serialize(object) {
    return queryString.stringify(object, {
      skipNulls: true
    })
  },
  serializeMulti(object) {
    let mergedObj = {};
    (_.values(object)).forEach(obj => {
      _.extend(mergedObj, obj);
    });
    return queryString.stringify(mergedObj, {
      skipNulls: true
    })
  }

}
