import Vue from 'vue/dist/vue.js';
import App from './App.vue';
import store from './store';
import VueMqtt from 'vue-mqtt';
import VueMqttOptions from './VueMqttOptions.js';

Vue.config.productionTip = false

Vue.use(VueMqtt, 'mqtt://192.168.1.23', options);

const app = new Vue({
    el: '#app',

    store,

    components: {
        'app': App
    },

    computed: {},

    watch: {},

    beforeCreate() {},

    created() {},

    beforeMount() {},

    mounted() {},

    beforeUpdate() {},

    updated() {},

    methods: {},
});
