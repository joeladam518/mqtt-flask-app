<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss" scoped>
    .card-body{
        min-height: 200px;
    }
</style>

<template>
    <div class="card monitor-section">
        <div class="card-header">
            subscribed topics
        </div>
        <div class="card-body">
            <div v-show="subscribed_topics.length > 0">
                <ul>
                    <li v-for="(topic, index) in subscribed_topics" :key="makeKey()">
                        <span>{{ topic }} </span>
                        <a @click.stop.prevent="mqttUnsubscribeTopic(topic)" href="#" class="btn btn-default">
                            unsubscribe
                        </a>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>

<script>
import { mapState, mapMutations } from 'vuex';
import { makeKey } from 'site_helpers';
export default {
    name: 'show-subscribed-topics',

    components: {

    },

    data() {
        return {
            //
        }
    },

    computed: {
        ...mapState({
            subscribed_topics: state => state.subscribed_topics,
        }),
    },

    watch: {},

    beforeCreate() {},

    created() {},

    beforeMount() {},

    mounted() {},

    beforeUpdate() {},

    updated() {},

    methods: {
        makeKey,
        ...mapMutations([
            'unsubscribe'
        ]),
        mqttUnsubscribeTopic(this_topic) {
            console.log('this_topic: ', this_topic);
            this.unsubscribe(this_topic);
        },
    },
}
</script>


