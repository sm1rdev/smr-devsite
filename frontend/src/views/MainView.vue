<script setup>
  import { reactive, onMounted } from 'vue';
  import { useI18n } from 'vue-i18n'
  import api from '../app/api/index';
  import Header from '../components/Header.vue';
  import Project from '../components/Project.vue';
  import Link from '../components/Link.vue';


  const { t } = useI18n()

  const projects = reactive([]);
  const links = reactive([])


  async function loadProjects() {
    try {
      const response = await api.get("/projects", {
        params: {
          page: 1
        }
      });
      projects.value = response.data.results;
    } catch(e) {
      console.error(e);
    }
  }

  async function loadSocials() {
    try {
      const response = await api.get("/links/");
      links.value = response.data;
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

      <n-card :title="t('projects')" size="large"
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

      <n-card :title="t('links')" size="large"
        :theme-overrides="{
          titleTextColor: '#ffffff'
        }"
        style="background-color: #202020; margin: 0 auto 20px; max-width: 920px; border: none; border-radius: 9px;">
        <n-list :theme-overrides="{
          borderColor: 'transparent'
        }" style="background-color: transparent;"
        v-for="(link, index) in links.value" :key="index">
          <Link :name="link.name" :fab_icon="link.fab_icon" :url="link.url"/>
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
