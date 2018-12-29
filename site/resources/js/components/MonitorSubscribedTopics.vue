<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss" scoped>
    .card-body{
        min-height: 200px;
    }
</style>

<template>
    <div class="card monitor-section">
        <div class="card-header">
            received messages
            <a @click.stop.prevent="clearMqttMessages" href="#" class="btn btn-default">clear messages</a>
        </div>
        <div class="card-body">
            <div v-show="received_messages.length > 0">
                <ul>
                    <li v-for="(message, index) in received_messages" :key="makeKey()">{{ message }}</li>
                </ul>
            </div>
        </div>
    </div>
</template>

<script>
import { mapState, mapMutations } from 'vuex';
import { makeKey } from 'site_helpers';
export default {
    name: 'monitor',

    components: {

    },

    data() {
        return {
            //
        }
    },

    computed: {
        ...mapState({
            received_messages: state => state.received_messages,
        }),
    },

    watch: {},

    beforeCreate() {},

    created() {},

    beforeMount() {},

    mounted() {},

    beforeUpdate() {},

    updated() {},

    // mqtt: {
    //     'tw1' (data) {
    //         this.receive_message('tw1: ' + data)
    //     },
    //     'tw2' (data) {
    //         this.receive_message('tw2: ' + data)
    //     },
    // },

    methods: {
        makeKey,
        ...mapMutations([
            'receive_message',
            'clear_received_message',
        ]),
        clearMqttMessages() {
            this.clear_received_message();
        },
    },
}
</script>


