<script setup>
    import { defineProps } from 'vue';

    const props = defineProps({
        name: String,
        fab_icon: String,
        link: String
    })
</script>

<template>
    <n-list-item>
        <div style="background-color: #2C2C2C; display: flex; flex-direction: column; border-radius: 9px;">

            <div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 20px;">

                <div style="display: flex; align-items: center; gap: 10px;">
                    <i :class="props.fab_icon" style="color: red;"></i>
                    <h3 style="color: white;">{{props.name}}</h3>
                </div>

                <div>
                    <n-button class="custom-button" type="Default" tag="a" :href="props.link" target="_blank">
                        Go to link
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
