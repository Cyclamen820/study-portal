window.MathJax = {
  // ★以下の loader と tex.packages を追加して mhchem を読み込む
  loader: {load: ['[tex]/mhchem']},
  tex: {
    packages: {'[+]': ['mhchem']},
    // 以下は先ほど設定したまま
    inlineMath: [["\\(", "\\)"], ["$", "$"]],
    displayMath: [["\\[", "\\]"], ["$$", "$$"]],
    processEscapes: true,
    processEnvironments: true
  }
};

document$.subscribe(() => {
  MathJax.startup.output.clearCache()
  MathJax.typesetClear()
  MathJax.texReset()
  MathJax.typesetPromise()
})