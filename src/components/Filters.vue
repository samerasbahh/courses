<template>
  <div class="flex flex-wrap mb-8">
    <b-container fluid>
      <b-row>
        <b-col sm="2" v-for="filter in filters" :key="filter.name+'-'+filter.type">
          <DatePicker
            v-if="filter.type === 'time'"
            :key="filter.name+'-'+filter.type"
            lang="en"
            type="time"
            :value="filter.value"
            :clear-button="true"
            format="HH:mm"
            :placeholder="filter.label"
            value-type="format"
            @cleared="handleClear(filter.name)"
            @input="handleTextInputChange(filter.name,$event)"
          />
          <TextInput
            v-else
            :key="filter.name+'-'+filter.type"
            :type="filter.type"
            input-class=""
            wrapper-class=""
            :has-remove="true"
            :placeholder="filter.label"
            :value="filter.value"
            @clear="handleClear(filter.name)"
            @input="handleTextInputChange(filter.name,$event)"
            @apply="$emit('apply')"
          />
        </b-col>
      </b-row>
      <b-row>
        <b-button class="search-btn mx-auto" variant="outline-primary" @click="$emit('apply')">
          <font-awesome-icon
            icon="search"
            size="xs"/>
          Search
        </b-button>
      </b-row>
    </b-container>

  </div>
</template>

<script>
  import TextInput from './TextInput'
  import {library} from '@fortawesome/fontawesome-svg-core'
  import {faSearch} from '@fortawesome/free-solid-svg-icons'
  import DatePicker from 'vue2-datepicker'

  library.add(faSearch);

  export default {
    /**
     * all props have their needed types
     * and are passed using the mixin
     */
    props: {
      filters: {
        type: Array,
        default: () => ([])
      },
    },
    components: {TextInput, DatePicker},
    data() {
      return {
        val: ''
      }
    },

    methods: {
      options(options) {
        return options.filter(option => {
          return option.label !== ""
        })
      },
      handleClear(name, value = null) {
        this.$emit('change', {
          name,
          value: value
        })
      },
      handleTextInputChange(name, value) {
        this.$emit('change', {
          name,
          value
        })
      },

    }

  }
</script>

<style lang="scss">
  @import '../sass/_filters.scss';
</style>
