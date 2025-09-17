<script setup>
  import { ref, computed } from "vue";
  import { useI18n } from "vue-i18n";
  const { locale } = useI18n()
  const showLanguageSelect = ref(false);
  const currentLang = ref('en');


  const options = computed(() => [
    {
      label: "EN",
      key: "en",
      disabled: currentLang.value === 'en'
    },
    {
      label: "RU",
      key: "ru",
      disabled: currentLang.value === 'ru'
    }
  ])

  const currentFlag = computed(() =>
    new URL(`../assets/icons/${currentLang.value}.png`, import.meta.url).href
  )

  const currentArrow = computed(() =>
    new URL(`../assets/icons/${showLanguageSelect.value ? 'arrow-up' : 'arrow-down'}.png`, import.meta.url).href
  )

  function selectLang(key) {
    currentLang.value = key;
    locale.value = key
  }
</script>

<template>
    <n-layout-header
      style="background-color: #202020; color: #FFF833; padding: 0 20px; display: flex; align-items: center; justify-content: center; height: 50px;">

      <h1
        style="margin: 0; font-family: 'Cyberverse', sans-serif; font-weight: 700; font-style: italic; font-size: 24px;">
        SMR DEVSITE</h1>

      <n-dropdown trigger="click" :options="options" @select="selectLang" @update:show="showLanguageSelect = $event"
        style="background-color: #191919;"
        :theme-overrides="{
          optionTextColor: '#FFFFFF',
          optionTextColorHover: '#191919',
          optionColorHover: '#FFF833'
        }">
        <div style="position: absolute; right: 20px; cursor: pointer; display: flex; gap: 10px; padding: 5px;">
          <img alt="Language selector" :src="currentFlag" height="24px" width="24px"/>
          <img :src="currentArrow" height="24px" width="24px"/>
        </div>
      </n-dropdown>

    </n-layout-header>
</template>

<style scoped>

</style>
