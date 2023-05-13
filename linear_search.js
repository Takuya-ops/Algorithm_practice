var fruits = ["Apple", "Orange", "Nuts", "Grape", "Banana"];

// 対象の文字列がある場合、そのインデックス番号を返す
console.log(fruits.indexOf("Banana"));

// 対象の文字列がある場合、そのインデックス番号を返す（ない場合は、-1が返される。）
console.log(fruits.indexOf("Bananaa"));

// 条件式を使って対象のindexを返す
console.log(fruits.findIndex(function(item) {
  return item === "Banana";
}));

// 条件式を使って対象のindexを返す（ない場合は-1が返される。）
console.log(fruits.findIndex(function(item) {
  return item === "Bananaa";
}));

// 対象の文字列が存在する場合、その文字を返す
console.log(fruits.find(function(item) {
  return item === "Banana";
}));

// 対象の文字列が存在する場合、その文字を返す。（ない場合は、undefinedが返される）
console.log(fruits.find(function(item) {
  return item === "Bananaa";
}));

// 真偽値を返す（true）
console.log(fruits.includes("Banana"));

// 真偽値を返す（false）
console.log(fruits.includes("Bananaa"));