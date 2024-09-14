const webglGetParameter = WebGLRenderingContext.prototype.getParameter;
const webglHandler = function (parameter) {
  if (parameter === 37445) {
    return "Google Inc. (NVIDIA)";
  }
  if (parameter === 37446 || parameter === 7937) {
    return "ANGLE (NVIDIA, NVIDIA GeForce GTX 660 Direct3D11 vs_5_0 ps_5_0, D3D11)";
  }
  return webglGetParameter.call(this, parameter); // webglGetParameter(parameter);
};

WebGLRenderingContext.prototype.getParameter = webglHandler.bind(webglGetParameter)