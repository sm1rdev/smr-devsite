<script setup>
    import { defineProps } from 'vue';
    import { useI18n } from 'vue-i18n';
    import { get_fab_icon } from '../app/icons/index';


    const { t } = useI18n();

    const props = defineProps({
        name: String,
        fab_icon: String,
        url: String
    })
</script>

<template>
    <n-list-item>
        <div style="background-color: #2C2C2C; display: flex; flex-direction: column; border-radius: 9px;">

            <div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 20px;">

                <div style="display: flex; align-items: center; gap: 10px;">
                    <i :class="get_fab_icon(props.fab_icon).fab_icon" :style="`color: ${get_fab_icon(props.fab_icon).color}`"></i>
                    <h3 style="color: white;">{{props.name}}</h3>
                </div>

                <div>
                    <n-button class="custom-button" type="Default" tag="a" :href="props.url" target="_blank">
                        {{t('go to link')}}
                    </n-button>
                </div>

            </div>

        </div>

    </n-list-item>
</template>

<style scoped>
.custom-button {
    background-color: #3179FF !important;
    color: #fff !important;
    outline: none;
    transition: all 0.3s ease;
}
.custom-button:hover {
    background-color: #255fc1 !important;
}
.custom-button:active {
    background-color: #1f4fa3 !important;
    transform: scale(0.96);
}
</style>
