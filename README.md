<h1>Battle RPG Simulation</h1>
<p>This is a simple simulation of a battle RPG-style game where the player controls a hero and battles against monsters. The game is turn-based, where the player chooses an action and then the monster takes its turn.</p>
<h2>Getting Started</h2>
<ol>
  <li>Clone the repository</li>
  <li>Open the terminal and navigate to the project folder</li>
  <li>Run the command <code>python game.py</code> to start the game</li>
</ol>
<h2>How to Play</h2>
<ol>
  <li>You will be prompted to select a monster to battle against.</li>
  <li>You control a hero character who has a health of 100 and an attack of 50.</li>
  <li>The monster has its own set of attributes, including health, damage, and energy.</li>
  <li>During each turn, you can select from four actions:
    <ol>
      <li>Attack: Deals damage to the monster based on your hero's attack.</li>
      <li>Defend: You defend yourself and heal 2 health points.</li>
      <li>Do Nothing: The monster will attack you, and you will take damage.</li>
      <li>Escape: You try to escape from the battle. If your hero's attack is higher than the monster's damage, you can escape successfully; otherwise, you must continue the battle.</li>
    </ol>
  </li>
  <li>The battle ends when either you or the monster's health points drop to zero.</li>
</ol>
<h2>Classes</h2>
<h3>Hero</h3>
<p>The <code>Hero</code> class represents the player character. It has the following attributes:</p>
<ul>
  <li><code>health</code>: the health points of the hero (default: 100)</li>
  <li><code>damage</code>: the damage points of the hero's attack (default: 50)</li>
</ul>
<p>The <code>Hero</code> class has the following methods:</p>
<ul>
  <li><code>attack()</code>: deals damage to the target (the monster)</li>
  <li><code>setTarget(target)</code>: sets the target of the hero's attack</li>
  <li><code>heal(amount)</code>: heals the hero by the specified amount</li>
</ul>
<h3>Monster</h3>
<p>The <code>Monster</code> class represents the enemy. It has the following attributes:</p>
<ul>
  <li><code>auto_attack</code>: the damage points of the monster's attack (default: 15)</li>
  <li><code>health</code>: the health points of the monster (default: 100)</li>
  <li><code>energy</code>: the energy points of the monster (default: 100)</li>
</ul>
<p>The <code>Monster</code> class has the following methods:</p>
<ul>
  <li><code>get_damage(amount)</code>: reduces the monster's health by the specified amount</li>
  <li><code>autoAttack(target)</code>: the monster's attack (automatic)</li>
  <li><code>move(speed)</code>: moves the monster at the specified speed</li>
  <li><code>attributes()</code>: prints out the monster's attributes</li>
</ul>
<h3>Fish</h3>
<p>The <code>Fish</code> class represents a fish. It has the following attributes:</p>
<ul>
  <li><code>speed</code>: the speed of the fish</li>
  <li><code>has_scales</code>: whether the fish has scales or not</li>
</ul>
<h3>Shark</h3>
<p>The <code>Shark</code> class inherits from the <code>Monster</code> and <code>Fish</code> classes. It has the following attributes:</p>
<ul>
  <li><code>bite_strength</code>: the bite strength of the shark</li>
  <li><code>health</code>: the health points of the shark</li>
  <li><code>energy</code>: the energy points of the shark</li>
  <li><code>speed</code>: the speed of the shark</li>
  <li><code>has_scales</code>: whether the shark has scales or not</li>
</ul>
<p>The <code>Shark</code> class has the following methods:</p>
<ul>
  <li><code>bite(target)</code>: deals damage to the target (the hero)</li>
  <li><code>move()</code>: moves the shark</li>
</ul>
<h3>Scorpion</h3>
<p>The <code>Scorpion</code> class inherits from the <code>Monster</code> class. It has the following attributes:</p>
<ul>
  <li><code>poison_damage</code>: the poison damage of the scorpion</li>
  <li><code>health</code>: the health points of the scorpion</li>
  <li><code>energy</code>: the energy points of the scorpion</li>
</ul>
<p>The <code>Scorpion</code> class has the following methods:</p>
<ul>
  <li><code>autoAttack(target)</code>: the scorpion's attack (poisonous)</li>
</ul>
