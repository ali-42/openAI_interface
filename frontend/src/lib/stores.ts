import { writable } from "svelte/store"

export const logged = writable(0);
export const currentUser = writable('');
