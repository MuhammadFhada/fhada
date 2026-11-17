export default {
  async fetch(request, env, ctx) {
    return new Response("Halo, Cloudflare Worker saya sudah aktif!");
  },
};
