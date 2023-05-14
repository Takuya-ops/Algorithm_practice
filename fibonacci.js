// フィボナッチ数列の実装（O(2^n)） → 単純に実装した場合
// 計算回数を標示させる用
let calculationsNormal = 0

function fibonacci(n) {
  // インデックス番号が-にならないように条件式をつける
  calculationsNormal++;
  if (n < 2) {
    return n
  };
  // 前の２つの数字を足し合わせる
  return fibonacci(n-1) + fibonacci(n-2);
};

console.log("normal:", fibonacci(45));
console.log("cacheを使わなかった場合:計算回数は" + calculationsNormal + "回です。")


// Dynamic Programmingで実装した場合 → O(n)
// 計算回数を表示させる用
let calculationsMod = 0

function fibonacciMod() {
  // 空のキャッシュを作成
  let cache = {};
  // クロージャーを使用
  return function fib(n) {
    // 参考に計算回数を表示させる。
    calculationsMod++;
    // cacheの中に数字があれば、それを使用する
    if (n in cache) {
      return cache[n];
      // なければ、キャッシュに保存する
    } else {
      // 保存する値を明示
      // インデックス番号nが0, 1の時はn-2が負の数になってしまうため、インデックス番号(n)をそのまま返す。
      if (n < 2) {
        return n;
      // それ以外の時（n >= 2）は、２つ前と１つ前の値を足したものを返す。
      } else {
        cache[n] = fib(n-1) + fib(n-2);
        return cache[n];
      }
    }
  }
};

// おまけ：ボトムアップ・アプローチ
// 計算回数用
let calculationsMod2 = 0;

function fibonacciMod2(n) {
  // 初期のリストを定義
  let answer = [0, 1];
  for (let i = 2; i <= n; i++) {
    calculationsMod2++;
    answer.push(answer[i-2] + answer[i-1]);
  };
  return answer.pop();
};

// テスト
const fasterFib = fibonacciMod();
console.log("Dynamic Programming:", fasterFib(45));
console.log("cacheを使った場合:計算回数は" + calculationsMod + "回です。")
console.log("ボトムアップ・アプローチ:", fibonacciMod2(45));
console.log("ボトムアップ・アプローチを使った場合:計算回数は" + calculationsMod2 + "回です。")

// 再度ノーマルのファンクション
console.log("normal:", fibonacci(45));