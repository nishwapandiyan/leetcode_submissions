# 37. Sudoku Solver

[![LeetCode Link](https://img.shields.io/badge/LeetCode-Problem_Link-FFA116?style=flat-square&logo=leetcode)](https://leetcode.com/problems/sudoku-solver/)
![Difficulty](https://img.shields.io/badge/Difficulty-Hard-ef4444?style=flat-square)

## Problem Statement

<p>Write a program to solve a Sudoku puzzle by filling the empty cells.</p>

<p>A sudoku solution must satisfy <strong>all of the following rules</strong>:</p>

<ol>
	<li>Each of the digits <code>1-9</code> must occur exactly once in each row.</li>
	<li>Each of the digits <code>1-9</code> must occur exactly once in each column.</li>
	<li>Each of the digits <code>1-9</code> must occur exactly once in each of the 9 <code>3x3</code> sub-boxes of the grid.</li>
</ol>

<p>The <code>&#39;.&#39;</code> character indicates empty cells.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png" style="height:250px; width:250px" />
<pre>
<strong>Input:</strong> board = [[&quot;5&quot;,&quot;3&quot;,&quot;.&quot;,&quot;.&quot;,&quot;7&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;],[&quot;6&quot;,&quot;.&quot;,&quot;.&quot;,&quot;1&quot;,&quot;9&quot;,&quot;5&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;],[&quot;.&quot;,&quot;9&quot;,&quot;8&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;6&quot;,&quot;.&quot;],[&quot;8&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;6&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;3&quot;],[&quot;4&quot;,&quot;.&quot;,&quot;.&quot;,&quot;8&quot;,&quot;.&quot;,&quot;3&quot;,&quot;.&quot;,&quot;.&quot;,&quot;1&quot;],[&quot;7&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;2&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;6&quot;],[&quot;.&quot;,&quot;6&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;2&quot;,&quot;8&quot;,&quot;.&quot;],[&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;4&quot;,&quot;1&quot;,&quot;9&quot;,&quot;.&quot;,&quot;.&quot;,&quot;5&quot;],[&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;.&quot;,&quot;8&quot;,&quot;.&quot;,&quot;.&quot;,&quot;7&quot;,&quot;9&quot;]]
<strong>Output:</strong> [[&quot;5&quot;,&quot;3&quot;,&quot;4&quot;,&quot;6&quot;,&quot;7&quot;,&quot;8&quot;,&quot;9&quot;,&quot;1&quot;,&quot;2&quot;],[&quot;6&quot;,&quot;7&quot;,&quot;2&quot;,&quot;1&quot;,&quot;9&quot;,&quot;5&quot;,&quot;3&quot;,&quot;4&quot;,&quot;8&quot;],[&quot;1&quot;,&quot;9&quot;,&quot;8&quot;,&quot;3&quot;,&quot;4&quot;,&quot;2&quot;,&quot;5&quot;,&quot;6&quot;,&quot;7&quot;],[&quot;8&quot;,&quot;5&quot;,&quot;9&quot;,&quot;7&quot;,&quot;6&quot;,&quot;1&quot;,&quot;4&quot;,&quot;2&quot;,&quot;3&quot;],[&quot;4&quot;,&quot;2&quot;,&quot;6&quot;,&quot;8&quot;,&quot;5&quot;,&quot;3&quot;,&quot;7&quot;,&quot;9&quot;,&quot;1&quot;],[&quot;7&quot;,&quot;1&quot;,&quot;3&quot;,&quot;9&quot;,&quot;2&quot;,&quot;4&quot;,&quot;8&quot;,&quot;5&quot;,&quot;6&quot;],[&quot;9&quot;,&quot;6&quot;,&quot;1&quot;,&quot;5&quot;,&quot;3&quot;,&quot;7&quot;,&quot;2&quot;,&quot;8&quot;,&quot;4&quot;],[&quot;2&quot;,&quot;8&quot;,&quot;7&quot;,&quot;4&quot;,&quot;1&quot;,&quot;9&quot;,&quot;6&quot;,&quot;3&quot;,&quot;5&quot;],[&quot;3&quot;,&quot;4&quot;,&quot;5&quot;,&quot;2&quot;,&quot;8&quot;,&quot;6&quot;,&quot;1&quot;,&quot;7&quot;,&quot;9&quot;]]
<strong>Explanation:</strong>&nbsp;The input board is shown above and the only valid solution is shown below:

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Sudoku-by-L2G-20050714_solution.svg/250px-Sudoku-by-L2G-20050714_solution.svg.png" style="height:250px; width:250px" />
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>board.length == 9</code></li>
	<li><code>board[i].length == 9</code></li>
	<li><code>board[i][j]</code> is a digit or <code>&#39;.&#39;</code>.</li>
	<li>It is <strong>guaranteed</strong> that the input board has only one solution.</li>
</ul>


---
*Synced automatically with [AlgoVault](https://github.com/mr-sanjai-offl/AlgoVault)*