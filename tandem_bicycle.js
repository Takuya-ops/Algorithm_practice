function tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest) {
  redShirtSpeeds.sort((a,b) => b - a);
  blueShirtSpeeds.sort((a,b) => fastest ? a - b : b - a);

  let result = 0;

  for (let index = 0; index < redShirtSpeeds.length; index++) {
    result += Math.max(redShirtSpeeds[index], blueShirtSpeeds[index]);
  }
  return result;
}

exports.tandemBicycle = tandemBicycle;