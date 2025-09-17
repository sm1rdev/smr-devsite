import { createI18n } from "vue-i18n";
import en from './en.json';
import ru from './ru.json';


const i18n = createI18n({
    legacy: false,
    locale: 'en',
    fallbackLocale: 'ru',
    messages: {
        en,
        ru,
    }
})

export default i18n
