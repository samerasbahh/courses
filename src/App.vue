<template>
  <div id="app">
    <h1>Courses Catalogue</h1>
    <div>
      <Datatable
        :isLoading="loading"
        :header="headers"
        :rows="rows"
        :filters="filters"
        :sorting="sorting"
        @sort="handleSort($event,loadData)"
        @filter="handleFilter($event)"
        @apply-filters="loadData()"

      ></Datatable>

    </div>
  </div>
</template>

<script>
  import {get as getCourses, getTableAtr as getCourseTableAttr} from './API/courseAPI'
  import sortingProvider from "./mixins/sortingProvider";
  import FiltersProvider from "./mixins/FiltersProvider";
  import formatTime from './helpers/helpers'

  export default {
    name: 'app',
    mixins: [sortingProvider, FiltersProvider],

    data() {
      return {
        loading: false,
        rows: [],
        headers: [],
        filters: [],
      }
    },
    mounted() {
      this.getTableAttr();
      this.loadData();
    },
    methods: {
      getTableAttr() {
        getCourseTableAttr().then(({data}) => {

          this.headers = data.headers;
          this.filters = data.filters;

        }).catch(error => {
          console.log('Error : ', error);
        });
      },
      formatData(data) {
        return data.map(object => {
          return {
            name: object.name,
            cost: object.cost,
            professor: object.professor.name,
            timeslots: object.timeslots.map(timeslot => {
              return `${timeslot.start_time} - ${timeslot.end_time}`;

            })
          }
        });
      },
      loadData({filters = {}, sorting = {}} = {}) {
        filters = filters && typeof filters === "object" ? filters : {}
        sorting = sorting && typeof sorting === "object" ? sorting : {}
        const params = {
          filters: {
            ...filters,
            ...this.filtersToParams()
          },
          sorting: {
            ...sorting,
            ...this.sortToParams(),
          }
        };
        this.loading = true;

        return getCourses(params).then(({data}) => {

          this.rows = this.formatData(data.results);

          this.loading = false;

        })
//          .catch(error => {
//            console.log('Error : ', error);
//          });
      },
    }
  }
</script>

<style lang="scss">
  @import './sass/_courses.scss';
</style>
