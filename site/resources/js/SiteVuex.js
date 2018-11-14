import Vue from 'vue';
import Vuex from 'vuex';
import VueMqtt from 'vue-mqtt';
import VueMqttOptions from './VueMqttOptions.js';

Vue.use(Vuex);
Vue.use(VueMqtt, 'ws://192.168.1.23:9001', VueMqttOptions);

let mqttVuer = new Vue();

const state = {
    subscribed_topics: [],
    received_messages: [],
};

const getters = {
    subscribed_topics: state => state.subscribed_topics,
    received_messages: state => state.received_messages,
};

const mutations = {
    subscribe(state, topic) {
        let index = state.subscribed_topics.indexOf(topic);
        if (topic && index === -1) {
            mqttVuer.$mqtt.subscribe(topic)
            state.subscribed_topics.push(topic)
        }
    },
    unsubscribe(state, topic) {
        let index = state.subscribed_topics.indexOf(topic);
        if (index > -1) {
            mqttVuer.$mqtt.unsubscribe(topic);
            state.subscribed_topics.splice(index, 1);
        }
    },
    receive_message(state, message) {
        state.received_messages.push(message);
    },
    clear_received_message(state, message) {
        state.received_messages = [];
    },
};

const actions = {
    //
};

export default new Vuex.Store({
    state,
    getters,   // Getters retrieve information from the state
    mutations, // Mutations change values in the state and must be synchronous
    actions    // Actions trigger mutations and can be asynchronous
});
