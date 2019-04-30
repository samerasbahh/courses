<template>
  <!--
    input field that takes props from the user
    sets these props as shown below
    the type of input 'email, text, number'
    is passed in the 'type' prop.
    '@focus,@blur,@input,@change' are all
    events that are caught by the user
    in the original component.
    'inputClass' can be String, Array or Object
    and it is parsed and added to 'form-control '
    -->
  <div
    :class="`relative ${wrapperClass}`"
  >
    <input
      :type="type"
      :name="name"
      :value="value"
      :readonly="readOnly"
      :disabled="disabled"
      :maxlength="maxLength"
      :placeholder="placeholder"
      class="form-control"
      @blur="$emit('blur',$event.target.value)"
      @focus="$emit('focus',$event)"
      @change="$emit('change',$event)"
      @input="$emit('input',$event.target.value)"
      @keyup.enter="$emit('apply')"
    >
    <button
      v-if="hasRemove && value"
      class="clear-filter-button  "
      @click="$emit('clear')"
    >
      <font-awesome-icon
              icon="times"
              size="xs"/>
    </button>
  </div>
</template>


<script>
  import {library} from '@fortawesome/fontawesome-svg-core'
  import {faTimes} from '@fortawesome/free-solid-svg-icons'

  library.add(faTimes);
  export default {
    /**
     * all props have their needed types
     * and they also have their default
     * non-effecting values
     */
    props: {
      value: {
        type: [String, Number, Boolean],
        default: ''
      },
      size: {
        type: String,
        default: ''
      },
      type: {
        type: String,
        default: 'text'
      },
      placeholder: {
        type: String,
        default: 'Insert Text'
      },
      name: {
        type: String,
        default: ''
      },
      readOnly: {
        type: Boolean,
        default: false
      },
      maxLength: {
        type: Number,
        default: 100
      },
      disabled: {
        type: Boolean,
        default: false
      },
      hasRemove:{
        type: Boolean,
        default: false
      },
      wrapperClass:{
        type:String,
        default:''
      }
    }
  }
</script>

<style lang="scss">

</style>
