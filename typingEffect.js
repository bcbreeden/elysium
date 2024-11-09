// typingEffect.js

/**
 * Simulates a typing effect on the given element.
 * @param {HTMLElement} element - The DOM element where text will appear.
 * @param {string} text - The text to display with the typing effect.
 * @param {number} [speed=50] - The speed of typing (in milliseconds).
 */
function typeText(element, text, speed = 15) {
    element.innerHTML = "";  // Clear any existing content
    let i = 0;
  
    function type() {
      if (i < text.length) {
        element.innerHTML += text.charAt(i);
        i++;
        setTimeout(type, speed);
      }
    }
  
    type();
  }
  
  // Export function to make it available for import in other files
  export { typeText };