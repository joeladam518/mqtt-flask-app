<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss" scoped>
    .card-body{
        min-height: 85vh;
    }
</style>

<template>
    <div class="card monitor-section">
        <div class="card-header">
            monitor
        </div>
        <div class="card-body">
            <div v-show="subscribed_topics.length > 0">
                <h3>subscribed topics</h3>
                <ul>
                    <li v-for="(message, index) in subscribed_topics" :key="makeKey()">{{ message }}</li>
                </ul>
            </div>
            <div v-show="received_messages.length > 0">
                <h3>received messages</h3>
                <ul>
                    <li v-for="(message, index) in received_messages" :key="makeKey()">{{ message }}</li>
                </ul>
            </div>
        </div>
    </div>
</template>

<script>
import { mapState, mapMutations } from 'vuex';
export default {
    name: 'monitor',

    components: {

    },

    data() {
        return {
            subscribed_topics: [],
            received_messages: [],
        }
    },

    computed: {
        // ...mapState({
        //     subscribed_topics: state => state.subscribed_topics,
        //     received_messages: state => state.received_messages,
        // }),
    },

    watch: {},

    beforeCreate() {},

    created() {},

    beforeMount() {},

    mounted() {},

    beforeUpdate() {},

    updated() {},

    mqtt: {
        'tw1' (data) {
            this.received_messages.push('tw1: ' + data)
        },
        'tw2' (data) {
            this.received_messages.push('tw2: ' + data)
        },
    },

    methods: {
        // ...mapMutations([
        //     'receive_message'
        // ]),
        makeKey() {
            let text = "";
            let possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

            for (let i = 0; i < 7; i++) {
                text += possible.charAt(Math.floor(Math.random() * possible.length));
            }

            return text;
        },
    },
}
</script>


