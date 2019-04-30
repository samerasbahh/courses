import {$httpRequester} from '../helpers/httpRequester';
import queryString from'../helpers/QueryString'

export const get = (params = {}) => {
    return $httpRequester.get(`courses?${queryString.serializeMulti(params)}`)
};

export const getTableAtr = () => {
    return $httpRequester.get(`courses/table_attr?`)
};

export const update = (id, params) => {
    if (params instanceof FormData) {
        params.append('_method', 'put')
    } else if (params) {
        params._method = 'put'
    }
    return $httpRequester.post(`courses/${id}`, params, {
        headers: {
            'Content-Type': 'multipart/form-data'
        }
    })
};
export const create = (params = {}) => {
    return $httpRequester.post(`courses`, params, {
        headers: {
            'Content-Type': 'multipart/form-data'
        }
    })
};
