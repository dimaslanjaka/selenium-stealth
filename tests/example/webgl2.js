const webgl2GetParameter = WebGL2RenderingContext.prototype.getParameter;

const webgl2Handler = function (parameter) {
  if (parameter === 37445) {
    return "Google Inc. (NVIDIA)";
  }
  if (parameter === 37446 || parameter === 7937) {
    return "ANGLE (NVIDIA, NVIDIA GeForce GTX 660 Direct3D11 vs_5_0 ps_5_0, D3D11)";
  }
  return webgl2GetParameter.call(this, parameter); // Make sure 'this' refers to the WebGL2RenderingContext
};

WebGL2RenderingContext.prototype.getParameter = function (parameter) {
  return webgl2Handler.call(this, parameter); // Ensure 'this' is the WebGL context
};

// const iframes = [...window.top.document.querySelectorAll("iframe")];
// for (var i = 0; i < iframes.length; i++) {
//   if (iframes[i].contentWindow) {
//     if (iframes[i].contentWindow.WebGLRenderingContext) {
//       iframes[i].contentWindow.WebGLRenderingContext.prototype.bufferData = WebGLRenderingContext.prototype.bufferData;
//       iframes[i].contentWindow.WebGLRenderingContext.prototype.getParameter = WebGLRenderingContext.prototype.getParameter;
//     }
//     if (iframes[i].contentWindow.WebGL2RenderingContext) {
//       iframes[i].contentWindow.WebGL2RenderingContext.prototype.bufferData = WebGL2RenderingContext.prototype.bufferData;
//       iframes[i].contentWindow.WebGL2RenderingContext.prototype.getParameter = WebGL2RenderingContext.prototype.getParameter;
//     }
//   }
// }