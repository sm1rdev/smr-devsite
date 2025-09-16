<script setup>
  import { reactive, onMounted } from 'vue';
  import api from '../app/api';
  import Header from '../components/Header.vue';
  import Project from '../components/Project.vue';
  import Social from '../components/Social.vue';


  const projects = reactive([]);
  const socials = reactive([])


  async function loadProjects() {
    try {
      const response = await api.get("/projects/");
      projects.value = response.data;
    } catch(e) {
      console.error(e);
    }
  }

  async function loadSocials() {
    try {
      const response = await api.get("/socials/");
      socials.value = response.data;
    } catch(e) {
      console.error(e);
    }
  }

  onMounted(async () => {
    await loadProjects();
    await loadSocials();
  })
</script>

<template>
  <n-layout style="min-height: 100vh; display: flex; flex-direction: column; background-color: #191919;">

    <!-- Header -->
    <Header></Header>

    <!-- Content -->
    <n-layout-content style="background-color:#191919; color: white; flex: 1; padding: 20px;">

      <n-card title="Projects" size="large"
        :theme-overrides="{
          titleTextColor: '#ffffff'
        }"
        style="background-color: #202020; margin: 0 auto 20px; max-width: 920px; border: none; border-radius: 9px;">
        <n-list class="custom-scroll" :theme-overrides="{
          borderColor: 'transparent'
        }" style="background-color: transparent; max-height: 60vh; overflow-y: auto; scroll-behavior: smooth; padding-right: 10px;"
        v-for="(project, index) in projects.value" :key="index">

          <Project :title="project.name" :tags="project.tags" :links="project.links" :description="project.description"/>

        </n-list>
      </n-card>

      <n-card title="Links" size="large"
        :theme-overrides="{
          titleTextColor: '#ffffff'
        }"
        style="background-color: #202020; margin: 0 auto 20px; max-width: 920px; border: none; border-radius: 9px;">
        <n-list :theme-overrides="{
          borderColor: 'transparent'
        }" style="background-color: transparent;"
        v-for="(social, index) in socials.value" :key="index">
          <Social :name="social.name" :fab_icon="social.fab_icon" :link="social.link"/>
        </n-list>
      </n-card>

    </n-layout-content>

    <!-- Footer -->
    <n-layout-footer style="background-color: #202020; color: #FFF833; text-align: center; padding: 10px;">
      @smr_dela © 2025
    </n-layout-footer>
  </n-layout>
</template>

<style scoped>

</style>
