const celebrities = {
    'Tom Cruise': 59,
    'Jennifer Lawrence': 31,
    'Justin Bieber': 28,
    'Beyonce': 40,
    'Kanye West': 44,
    'Taylor Swift': 32,
    'Ariana Grande': 28,
    'Dwayne Johnson': 49,
    'Selena Gomez': 29,
    'Kendall Jenner': 26
  };
  
  let celebLeft, celebRight;
  let score = 0;
  
  function get_random_celebrities() {
    const celebs = Object.keys(celebrities);
    celebLeft = celebs[Math.floor(Math.random() * celebs.length)];
    celebRight = celebs[Math.floor(Math.random() * celebs.length)];
    while (celebLeft === celebRight) {
      celebRight = celebs[Math.floor(Math.random() * celebs.length)];
    }
    document.getElementById('celeb-left').textContent = celebLeft;
    document.getElementById('celeb-right').textContent = celebRight;
  }
  
  function check_guess(guess) {
    if (celebrities[celebRight] > celebrities[celebLeft] && guess === 'higher') {
      score++;
      document.getElementById('result').textContent = 'Correct!';
    } else if (celebrities[celebRight] < celebrities[celebLeft] && guess === 'lower') {
      score++;
      document.getElementById('result').textContent = 'Correct!';
    } else {
      document.getElementById('result').textContent = 'Game over!';
      document.getElementById('score').textContent = `Your final score is ${score}`;
      score = 0;
    }
    document.getElementById('score').textContent = `Score: ${score}`;
    get_random_celebrities();
  }
  
  document.getElementById('higher-btn').addEventListener('click', () => check_guess('higher'));
  document.getElementById('lower-btn').addEventListener('click', () => check_guess('lower'));
  
  get_random_celebrities();
  