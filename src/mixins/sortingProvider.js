export default {
  data() {
    return {
      sorting: {
        type: null,
        column: null
      }
    }
  },
  methods: {
    sortToParams() {
      if(this.sorting.column){
        return {ordering: `${this.sorting.type === 'asc' ? '' : '-'}${this.sorting.column}`}
      }
      return {};
    },
    handleSort(column, callback) {

      this.sorting = {
        column: column,
        type: this.sorting.type === 'asc' ? 'desc' : 'asc'
      };

      if (callback && typeof callback === 'function') {
        callback()
      }

    }
  },
}
