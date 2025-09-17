import fab_icons from './icons.json'


export function get_fab_icon(name) {
    return fab_icons.find(item => item.name === name) ?? fab_icons.find(item => item.name === "default");
}
