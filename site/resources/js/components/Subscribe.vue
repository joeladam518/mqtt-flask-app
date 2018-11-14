<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

</style>

<template>
    <div class="card subscribe-section">
        <div @click="toggleCardBody" class="card-header" >
            subscribe to mqtt topics
        </div>
        <div v-show="showCardBody" class="card-body">
            <form id="mqtt-subscribe-topic-form" class="mqtt-form" action="#" method="POST" @submit.stop.prevent="mqttSubscribeTopic">

                <div class="form-group row">
                    <label for="topic" class="col-md-4 col-form-label text-md-right">
                        Topic
                    </label>

                    <div class="col-md-8" >
                        <input type="text" class="form-control" id="topic" name="topic" v-model="topic" required autofocus>
                    </div>
                </div>

                <div class="form-group row mb-0 submit-wrap">
                    <button type="submit" class="btn btn-primary">
                        subscribe
                    </button>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
import { mapMutations } from 'vuex';
export default {
    name: 'subscribe',

    components: {

    },

    props: {
        showThis: {
            type: Boolean,
            default() {
                return true
            },
        },
    },

    data() {
        return {
            topic: '',
            showCardBody: this.showThis,
        }
    },

    computed: {},

    watch: {},

    beforeCreate() {},

    created() {},

    beforeMount() {},

    mounted() {},

    beforeUpdate() {},

    updated() {},

    methods: {
        ...mapMutations([
            'subscribe'
        ]),
        toggleCardBody() {
            this.showCardBody = !this.showCardBody;
        },
        mqttSubscribeTopic() {
            this.subscribe(this.topic);
            this.clearInputs();
        },
        clearInputs() {
            this.topic = '';
        }
    },
}
</script>


