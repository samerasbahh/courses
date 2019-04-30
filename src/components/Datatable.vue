<template>
  <div class="">
    <loading :active.sync="isLoading"
             :can-cancel="false"
             :is-full-page="isLoading">

    </loading>
    <div
      class="table-container-main overflow-auto pl-2 mb-2"
    >
      <Filters
        v-if="filters.length > 0"
        :filters="filters"
        @change="$emit('filter',$event)"
        @apply="$emit('apply-filters')"
      />
      <table
        :class="[`table table-striped main-table w-full text-left  scrollable-fixed-header mb-8`]"
      >
        <thead>
        <tr class="font-bold">
          <th
            v-for="head in header"
            :key="head.name"
            class="pl-6 text-xs  whitespace-no-wrap relative cursor-pointer"
            @click="handleSort(head)"
          >
              <span>
                {{ head.label }}
              </span>
            <font-awesome-icon
              v-if="head.sortable"
              :icon="`${sorting.column === null || sorting.column !== head.name ? 'sort' : (sorting.column === head.name && sorting.type === 'asc' ? 'sort-up' :'sort-down')}`"
              size="xs"/>

          </th>
        </tr>
        </thead>

        <tbody>
        <tr
          v-if="rows.length > 0"
          v-for="row in rows"
          :key="row.id"
          class="font-bold text-black  border-grey-light border-b-2"
        >

          <td
            v-for="head in header"
            :key="head.name"
            class="py-4 pl-6 text-sm "
          >
            <span v-if="Array.isArray(getRowValue(row, head))"
                  v-for="el in getRowValue(row, head)"
                  class="td-multiple">
                {{el}}
            </span>
            <span
              v-if="!Array.isArray(getRowValue(row, head))"
              dir="auto"
              class="whitespace-no-wrap"
            >
                {{ getRowValue(row, head) }}
              </span>
          </td>

        </tr>
        <tr v-else> No data to be shown</tr>

        </tbody>

      </table>
    </div>

  </div>
</template>


<script>
  import {library} from '@fortawesome/fontawesome-svg-core'
  import {faSort, faSortUp, faSortDown} from '@fortawesome/free-solid-svg-icons'
  import Filters from './Filters.vue'

  // Import component
  import Loading from 'vue-loading-overlay';
  // Import stylesheet
  import 'vue-loading-overlay/dist/vue-loading.css';

  library.add(faSort, faSortDown, faSortUp);
  export default {
    /**
     * all props have their needed types
     * and are passed using the mixin
     */
    props: {
      isLoading: {
        type: Boolean,
        default: false
      },
      sorting: {
        type: Object,
        default: () => ({})
      },
      header: {
        type: Array,
        default: () => []
      },
      rows: {
        type: Array,
        default: () => []
      },
      filters: {
        type: Array,
        default: () => []
      }
    },
    components: {Filters, Loading},
    methods: {
      getRowValue(row, {valueHandler, name}) {
        return row[name];
      },
      handleSort(head) {
        if (head.sortable) {
          this.$emit('sort', head.name)
        }
      }
    }
  }
</script>

<style lang="scss">
  @import '../sass/_datatable.scss';
</style>
