<script setup>
    import { ref, computed, defineProps } from 'vue';
    const showContent = ref(false);

    const props = defineProps({
        title: String,
        tags: Array,
        links: Array,
        description: String
    })


    const currentArrow = computed(() =>
        new URL(`../assets/icons/${showContent.value ? 'arrow-up' : 'arrow-down'}.png`, import.meta.url).href
    )

    function openContent() {
        showContent.value = !showContent.value
    }
</script>

<template>
    <n-list-item>
        <div style="background-color: #2C2C2C; display: flex; flex-direction: column; border-radius: 9px;">

            <div
                style="display: flex; justify-content: space-between; align-items: center; padding: 20px;">

                <div>
                    <h3 style="margin: 0 0 10px 0; color: white;">{{props.title}}</h3>
                    <n-space>
                        <n-tag type="info" v-for="(tag, index) in props.tags" :key="index">{{tag}}</n-tag>
                    </n-space>
                </div>

                <div style="display: flex; align-items: center; gap: 10px;">
                    <n-button text tag="a" :href="link.link" target="_blank" style="padding: 5px;"
                    v-for="(link, index) in props.links" :key="index">
                        <template #icon>
                            <i :class="link.fab_icon" style="color: white;"></i>
                        </template>
                    </n-button>

                    <n-button text @click="openContent" style="padding: 5px;">
                        <img :src="currentArrow" height="24px" width="24px"/>
                    </n-button>
                </div>

            </div>

            <div v-if="showContent" style="display: flex; justify-content: space-between; align-items: center; padding: 0 20px 20px 20px;">
                
                <div class="project-description" style="flex: 1; margin: 20px; color: white; text-align: center;">
                    {{ props.description }}
                </div>
                
            </div>

        </div>
        
    </n-list-item>
</template>

<style scoped>
</style>
