window.Vue = require('vue');
window.Vuex = require('vuex');

import BootstrapVue from 'bootstrap-vue';
import MainVue from './MainVue.vue';

/**
 * Load the vue plugins
 */
Vue.use(BootstrapVue);

/**
 * Create the Vuex Store
 *
 * Notes:
 * The vue-mqtt plugin is initialized in the SiteVuex.js file
 */
import store from './SiteVuex';

/**
 * The main vue component
 */
Vue.component('main-vue', MainVue);

const vueApp = new Vue({
    el: '#app',

    store,

    computed: {},

    watch: {},

    beforeCreate() {},

    created() {},

    beforeMount() {},

    mounted() {
        //this.$mqtt.subscribe('VueMqtt/#')
        //this.$mqtt.subscribe(['tw1', 'tw2'])
    },

    beforeUpdate() {},

    updated() {},

    methods: {},
});
