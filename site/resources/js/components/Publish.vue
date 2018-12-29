    <!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

</style>

<template>
    <div class="card publish-section">
        <div @click="toggleCardBody" class="card-header">
            publish to mqtt topics
        </div>
        <div v-show="showCardBody" class="card-body">
            <form id="mqtt-publish-topic-form" class="mqtt-form" action="#" method="POST" @submit.stop.prevent="mqttPublishTopic">

                <div class="form-group row">
                    <label for="topic" class="col-md-4 col-form-label text-md-right">
                        Topic
                    </label>

                    <div class="col-md-8">
                        <input type="text" class="form-control" id="topic" name="topic" v-model="topic" required autofocus>
                    </div>
                </div>

                <div class="form-group row">
                    <label for="payload" class="col-md-4 col-form-label text-md-right">
                        mqtt messages
                    </label>

                    <div class="col-md-8">
                        <textarea class="form-control" id="payload" name="payload" v-model="payload" required></textarea>
                    </div>
                </div>

                <div class="form-group row mb-0 submit-wrap">
                    <button type="submit" class="btn btn-primary">
                        publish
                    </button>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
export default {
    name: 'publish',

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
            payload: '',
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
        mqttPublishTopic(event) {
            console.log('publish!')
            console.log('topic: ', this.topic);
            console.log('payload: ', this.payload)

            //this.$mqtt.publish(this.topic, this.payload)

            this.clearInputs();
        },
        toggleCardBody() {
            this.showCardBody = !this.showCardBody;
        },
        clearInputs() {
            this.topic = '';
            this.payload = '';
        }
    },
}
</script>


