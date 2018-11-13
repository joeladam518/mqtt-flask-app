import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        subscribed_topics: [],
        received_messages: [],
    },

    getters: {
        subscribed_topics: state => state.subscribed_topics,
        received_messages: state => state.received_messages,
    },

    mutations: {
        subscribe(state, topic) {
            if (topic) {
                //Vue.$mqtt.subscribe(topic)
                state.subscribed_topics.push(topic)
            }
        },
        unsubscribe(state, topic) {
            if (topic) {
                //Vue.$mqtt.unsubscribe(topic)
                let index = state.subscribed_topics.indexOf(topic);
                if (index > -1) {
                    state.subscribed_topics.splice(index, 1);
                }
            }
        },
        receive_message(state, message) {
            state.received_messages.push(message);
        },
    },

    actions: {
        //...
    },
})
