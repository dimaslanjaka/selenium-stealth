const webgl2GetParameter = WebGL2RenderingContext.prototype.getParameter;
const webgl2Handler = function (parameter) {
  if (parameter === 37445) {
    return "Google Inc. (NVIDIA)";
  }
  if (parameter === 37446 || parameter === 7937) {
    return "ANGLE (NVIDIA, NVIDIA GeForce GTX 660 Direct3D11 vs_5_0 ps_5_0, D3D11)";
  }
  return webgl2GetParameter.call(this, parameter); // webgl2GetParameter(parameter);
};

WebGL2RenderingContext.prototype.getParameter = webglHandler.bind(webgl2GetParameter)