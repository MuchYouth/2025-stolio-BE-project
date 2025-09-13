// 지속성 변수를 저장하기 위한 파일

import { writable } from 'svelte/store'

const persist_storage = (key, initValue) => {
    const storedValueStr = localStorage.getItem(key)
    const store = writable(storedValueStr != null ? JSON.parse(storedValueStr) : initValue)
    store.subscribe((val) => {
        localStorage.setItem(key, JSON.stringify(val))
    })
    return store
}

export const page = persist_storage("page", 0)
// 브라우저를 새로고침 하더라도 유지되어야 하는 변수 지정
export const access_token = persist_storage("access_token", "")
export const username = persist_storage("username", "")
export const is_login = persist_storage("is_login", false)
// 검색 후 확인하고 뒤로가기했을때 다시 검색된 페이지 보여주기위해서
export const keyword = persist_storage("keyword", "")