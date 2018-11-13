<style lang="scss">
  .card {
    margin: 20px auto;
  }
  .submit-wrap {
    display: flex;
    flex-flow: row nowrap;
    justify-content: flex-end;
    align-items: center;
    padding-right: 15px;
    padding-left: 15px;
  }
</style>

<template>
    <div class="container">
        <div class="row">
            <div class="col-md-12 col-lg-6">
                <publish :showCardBody="showForms"></publish>
                <subscribe :showCardBody="showForms"></subscribe>
                <unsubscribe :showCardBody="showForms"></unsubscribe>
            </div>
            <div class="col-md-12 col-lg-6">
                <monitor></monitor>
            </div>
        </div>
    </div>
</template>

<script>
import Publish from './components/Publish.vue'
import Subscribe from './components/Subscribe.vue'
import UnSubscribe from './components/UnSubscribe.vue'
import Monitor from './components/Monitor.vue'

export default {
    name: 'app',

    components: {
        'subscribe': Subscribe,
        'unsubscribe': UnSubscribe,
        'publish': Publish,
        'monitor': Monitor,
    },

    data() {
        return {
            showForms: true
        }
    },

    computed: {},

    watch: {},

    beforeCreate() {},

    created() {
        window.addEventListener('resize', this.handleResize)
    },

    beforeMount() {},

    mounted() {
        this.handleResize();
    },

    beforeUpdate() {},

    updated() {},

    beforeDestroy: function () {
        window.removeEventListener('resize', this.handleResize)
    },

    methods: {
        handleResize() {
            var width = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
            if (width < 992) {
                this.showForms = false;
            } else {
                this.showForms = true;
            }
        }
    },
}
</script>
