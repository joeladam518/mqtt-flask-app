import Vue from 'vue/dist/vue.js';
import App from './App.vue';
import store from './store';
import VueMqtt from 'vue-mqtt';
import VueMqttOptions from './VueMqttOptions.js';

Vue.config.productionTip = false

Vue.use(VueMqtt, 'ws://192.168.1.23:9001', VueMqttOptions);

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

    mounted() {
        //this.$mqtt.subscribe('VueMqtt/#')
        this.$mqtt.subscribe(['tw1', 'tw2'])
    },

    beforeUpdate() {},

    updated() {},

    methods: {},
});
