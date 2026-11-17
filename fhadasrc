
export default {
  async fetch(request) {
    const url = new URL(request.url);

    if (request.method === "GET" && url.pathname === "/") {
      return Response.json({
        status: "online",
        name: "My Agent"
      });
    }

    if (request.method === "GET" && url.pathname === "/health") {
      return Response.json({
        status: "healthy"
      });
    }

    if (request.method === "POST" && url.pathname === "/agent") {
      try {
        const data = await request.json();

        return Response.json({
          status: "success",
          response: "Agent received: " + data.message
        });
      } catch {
        return Response.json({
          error: "Invalid JSON"
        }, { status: 400 });
      }
    }

    return Response.json({
      error: "Not found"
    }, { status: 404 });
  }
};
