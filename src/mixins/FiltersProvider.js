import _ from 'underscore'

export default {
  data() {
    return {
      filters: [],
      filtersMap: {
        'text': '__icontains'
      }

    }
  },
  methods: {
    filtersToParams() {
      return this.filters.reduce((acc, filter) => {
        if (filter.value || filter.value === "") {
          acc[filter.name + this.getFilterMap(filter.type)] = filter.value
        }
        return acc
      }, {})
    },
    handleFilter(filterData, callback) {
      this.filters = this.filters.map(filter => {
        if (filter.name === filterData.name) {
          return {
            ...filter,
            value: filterData.value
          }
        }
        return filter;
      });
      if (typeof callback === 'function') {
        callback()
      }
    },
    getFilterMap(filterType) {
      if (_.has(this.filtersMap, filterType)) {
        return this.filtersMap[filterType];
      }
      return "";
    }

  },
}
