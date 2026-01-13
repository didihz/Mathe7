# CLAUDE.md - AI Assistant Guide for Mathe7 Repository

This document provides AI assistants with comprehensive information about the Mathe7 codebase structure, development workflows, and conventions.

## Project Overview

**Mathe7** is an educational mathematics learning platform designed for German-speaking 7th-grade students (Klasse 7). The project teaches proportional and antiproportional relationships (Zuordnungen) through interactive exercises, quizzes, and theory lessons.

### Core Educational Goals
- Teach students to recognize and differentiate between proportional and antiproportional relationships
- Provide adaptive learning with 5 difficulty levels
- Offer immediate feedback with detailed explanations
- Track student progress across sessions

### Technical Philosophy
The project demonstrates two key software engineering principles:
1. **Educational & Interactive Design**: Intuitive UIs, adaptive learning, immediate feedback
2. **Code Quality & Robustness**: Comprehensive error handling, input validation, clear error messages

## Three Application Versions

This project maintains **three distinct implementations** of the same learning application:

### 1. Standalone Browser Version (⭐ RECOMMENDED)
- **Files**: `index.html`, `app.js`, `static/css/style.css`
- **Technology**: Pure HTML/CSS/JavaScript
- **No Installation**: Just open `index.html` in a browser
- **Storage**: Browser LocalStorage for progress persistence
- **Deployment**: Static files, can run offline
- **Status**: Primary/recommended version

### 2. Flask Web Application (Optional)
- **Files**: `web_app.py`, `templates/*.html`, `static/*`, `START.py`
- **Technology**: Python Flask with Jinja2 templates
- **Server**: Flask development server on http://127.0.0.1:5000
- **Storage**: Flask sessions for progress tracking
- **Deployment**: Requires Python + Flask installation
- **Status**: Alternative server-based version

### 3. Desktop GUI Application (Optional)
- **Files**: `zuordnungen_app.py`, `START_HIER.py`, `start_app.sh/bat`
- **Technology**: Python tkinter
- **Platform**: Cross-platform desktop (Windows/Linux/macOS)
- **Storage**: In-memory progress (resets on close)
- **Deployment**: Requires Python + tkinter
- **Status**: Alternative native desktop version

## Repository Structure

```
Mathe7/
├── Documentation
│   ├── README.md                    # Main documentation (German)
│   ├── README_STANDALONE.md         # Standalone HTML/JS version docs
│   ├── README_WEB.md               # Flask web version docs
│   ├── README_APP.md               # Desktop GUI version docs
│   ├── ANLEITUNG.txt               # Quick start guide (German)
│   └── CLAUDE.md                   # This file - AI assistant guide
│
├── Standalone Browser Version (Primary)
│   ├── index.html                  # 286 lines - Main HTML page
│   ├── app.js                      # 680 lines - Client-side logic
│   └── static/
│       ├── css/style.css           # 1200+ lines - Styling
│       └── js/main.js              # 16 lines - Utilities
│
├── Flask Web Application
│   ├── web_app.py                  # 384 lines - Flask backend
│   ├── START.py                    # 71 lines - Web app launcher
│   └── templates/
│       ├── base.html               # Base template with navigation
│       ├── index.html              # Home/menu page
│       ├── theorie.html            # Theory sections
│       ├── quiz.html               # Quiz interface
│       ├── uebungen.html           # Exercises page
│       └── fortschritt.html        # Progress tracking page
│
├── Desktop GUI Application
│   ├── zuordnungen_app.py          # 1242 lines - Main tkinter app
│   ├── START_HIER.py               # 46 lines - Desktop launcher
│   ├── start_app.sh                # Unix/Linux launcher script
│   └── start_app.bat               # Windows launcher script
│
├── Math Utilities Library
│   ├── math_utils.py               # 319 lines - Math functions with error handling
│   └── test_math_utils.py          # 242 lines - Unit tests
│
└── Configuration
    ├── requirements.txt             # Python dependencies (Flask only)
    └── .gitignore                  # Git ignore patterns
```

## Technology Stack

### Frontend Technologies
- **HTML5**: Semantic markup, responsive structure
- **CSS3**: Modern styling with gradients, flexbox, responsive design
- **Vanilla JavaScript**: No frameworks, pure DOM manipulation
- **LocalStorage API**: Browser-based persistence

### Backend Technologies
- **Python 3.6+**: Core language
- **Flask 2.0+**: Web framework (optional, for web version only)
- **tkinter**: Built-in GUI toolkit (for desktop version)

### Development Tools
- **Git**: Version control
- **Bash/Batch**: Platform-specific launcher scripts

## Key Components Deep Dive

### Progress Tracking Object

All three versions share the same progress data structure:

```javascript
{
    level: 1,                    // Difficulty level (1-5)
    correct_answers: 0,          // Total correct answers
    total_attempts: 0,           // Total attempts made
    quiz_score: 0,               // Quiz score (out of 10)
    exercises_completed: 0,      // Number of exercises completed
    quiz_completed: false        // Whether quiz was completed
}
```

**Storage by Version:**
- Standalone: `localStorage.setItem('progress', JSON.stringify(progress))`
- Flask Web: `session['progress']` (server-side Flask sessions)
- Desktop GUI: `self.progress` (in-memory, class attribute)

### Adaptive Difficulty System

The application automatically adjusts difficulty based on performance:

**Level Up Criteria:**
- Accuracy > 70% (correct_answers / total_attempts)
- AND total_attempts >= 5
- Maximum level: 5

**Level Down Criteria:**
- Accuracy < 40%
- AND total_attempts >= 5
- Minimum level: 1

**Implementation Locations:**
- Standalone: `app.js` - `checkAnswer()` function
- Flask: `web_app.py` - `/api/check_answer` endpoint
- Desktop: `zuordnungen_app.py` - `check_answer()` method

### Exercise Generation by Level

Each level has specific exercise templates:

**Level 1:** Simple proportional problems
- Example: "2 eggs cost 0.80€. How much do 5 eggs cost?"

**Level 2:** More complex proportional
- Example: "A car drives 180 km in 2 hours. How far in 5 hours?"

**Level 3:** Antiproportional (workers/time)
- Example: "3 workers need 12 days. How many days for 4 workers?"

**Level 4:** Mixed difficult problems
- Example: Proportional/antiproportional with larger numbers

**Level 5:** Multi-step complex scenarios
- Example: Combined calculations requiring multiple steps

**Code Locations:**
- `app.js:220-400` - Standalone exercise generation
- `web_app.py:150-280` - Flask exercise generation
- `zuordnungen_app.py:450-650` - Desktop exercise generation

### Quiz Structure

**Format:**
- 10 questions total
- Question types: Proportional / Antiproportional / Neither
- Real-world scenarios (shopping, work, recipes, physics, etc.)
- Immediate feedback with detailed explanations
- Score tracking (out of 10)

**Question Pool:**
- 10 different questions hardcoded in each version
- Random selection ensures variety
- Each question includes:
  - `question`: The problem text
  - `answer`: Correct answer ('proportional', 'antiproportional', or 'neither')
  - `explanation`: Detailed explanation of why the answer is correct

### Theory Content (4 Sections)

1. **Was ist eine Zuordnung?** (What is a mapping?)
   - Basic concept introduction
   - Real-world examples

2. **Proportionale Zuordnungen** (Proportional relationships)
   - Definition: More → More, Less → Less
   - Constant quotient (Quotientengleichheit)
   - Formula: y₁/x₁ = y₂/x₂

3. **Antiproportionale Zuordnungen** (Antiproportional relationships)
   - Definition: More → Less, Less → More
   - Constant product (Produktgleichheit)
   - Formula: x₁ × y₁ = x₂ × y₂

4. **Wie erkenne ich die Art?** (How to recognize the type?)
   - Decision tree for identification
   - Examples of each type
   - Common pitfalls

## Math Utilities Module (`math_utils.py`)

This module demonstrates **professional error handling best practices**:

### Custom Exception Hierarchy

```python
MathError (base exception)
├── InvalidInputError      # Wrong type/format
├── DivisionError         # Division by zero
└── DomainError           # Invalid domain (e.g., sqrt of negative)
```

### Functions with Robust Error Handling

1. **`safe_divide(a, b)`**: Division with zero-check
2. **`calculate_average(numbers)`**: Average with validation
3. **`calculate_square_root(x)`**: Square root with domain checking
4. **`calculate_factorial(n)`**: Factorial with constraints
5. **`calculate_power(base, exponent)`**: Power with overflow checks
6. **`find_nth_element(lst, n)`**: Safe list indexing
7. **`calculate_percentage(part, whole)`**: Percentage calculation

**Error Handling Pattern:**
```python
def function_name(param):
    """Docstring with clear description"""
    # Type validation
    if not isinstance(param, expected_type):
        raise InvalidInputError("Clear error message")

    # Domain validation
    if param violates_constraint:
        raise DomainError("Clear error message")

    # Calculation with try/except for edge cases
    try:
        result = calculation()
    except Exception as e:
        raise MathError(f"Specific context: {e}")

    return result
```

## Development Workflows

### Making Changes to the Application

When modifying the learning application, you typically need to update **all three versions** to maintain feature parity:

#### Example: Adding a New Quiz Question

1. **Standalone (`app.js`)**:
   ```javascript
   // Add to quizQuestions array around line 50
   {
       question: "Your question text",
       answer: "proportional", // or "antiproportional" or "neither"
       explanation: "Detailed explanation"
   }
   ```

2. **Flask Web (`web_app.py`)**:
   ```python
   # Add to questions list in get_quiz_question() around line 74
   {
       'question': 'Your question text',
       'answer': 'proportional',
       'explanation': 'Detailed explanation'
   }
   ```

3. **Desktop GUI (`zuordnungen_app.py`)**:
   ```python
   # Add to self.quiz_questions around line 400
   {
       'question': "Your question text",
       'answer': 'proportional',
       'explanation': 'Detailed explanation'
   }
   ```

#### Example: Adding a New Exercise Level

1. Add new level templates to exercise generation functions in all three versions
2. Update maximum level constant (currently 5)
3. Adjust level up/down logic if needed
4. Test adaptive difficulty transitions

### Testing Changes

**Standalone Version:**
```bash
# No build required - just open in browser
open index.html
# or
python3 -m http.server 8000  # Then visit http://localhost:8000
```

**Flask Web Version:**
```bash
python3 START.py
# Or manually:
python3 -c "from web_app import app; app.run(debug=True)"
```

**Desktop GUI Version:**
```bash
python3 zuordnungen_app.py
# Or use launchers:
python3 START_HIER.py
bash start_app.sh
```

**Math Utils Testing:**
```bash
python3 test_math_utils.py
```

### Running Tests

The project currently uses manual testing with `test_math_utils.py`:

```bash
cd /home/user/Mathe7
python3 test_math_utils.py
```

**Test Coverage:**
- All 7 math utility functions
- Success cases
- Error cases (type errors, domain errors, edge cases)
- Manual output verification (no automated test framework)

### Git Workflow

**Current Branch:** `claude/add-claude-documentation-tkJ3p`

**Standard workflow:**
```bash
# Make changes to files
git add <changed-files>
git commit -m "Clear, descriptive message"

# Push to feature branch
git push -u origin claude/add-claude-documentation-tkJ3p
```

**Branch Naming Convention:**
- Feature branches: `claude/<description>-<session-id>`
- Must start with `claude/` for authentication
- Must end with matching session ID

**Commit Message Guidelines:**
- Use German or English (both acceptable)
- Be descriptive and concise
- Focus on the "why" rather than the "what"
- Examples:
  - "Add new quiz question about recipe proportions"
  - "Fix division by zero in exercise level 3"
  - "Update standalone version to match Flask features"

## Coding Conventions

### Python Conventions

**Style Guide:**
- Follow PEP 8 style guidelines
- Use 4 spaces for indentation
- Maximum line length: ~100 characters (flexible)
- Use docstrings for all functions and classes

**Naming:**
- Functions: `snake_case` (e.g., `calculate_average`)
- Classes: `PascalCase` (e.g., `ZuordnungenApp`)
- Constants: `UPPER_SNAKE_CASE` (if used)
- Private methods: `_leading_underscore`

**Type Hints:**
```python
from typing import List, Dict, Tuple

def function_name(param: int) -> float:
    """Clear docstring"""
    return result
```

**Error Handling:**
- Always use custom exceptions from `math_utils.py` hierarchy
- Provide clear, user-friendly error messages in German
- Validate inputs at function entry
- Use try/except for operations that might fail

### JavaScript Conventions

**Style Guide:**
- Use 4 spaces for indentation
- Use camelCase for variables and functions
- Use const/let (avoid var)
- Use template literals for strings with variables

**Naming:**
- Functions: `camelCase` (e.g., `checkAnswer`, `generateExercise`)
- Constants: `UPPER_SNAKE_CASE` (e.g., `MAX_LEVEL = 5`)
- DOM elements: descriptive names (e.g., `menuPage`, `quizPage`)

**Code Organization:**
- Initialize progress at top
- Helper functions before main logic
- Event listeners at bottom
- Clear comments for major sections

### HTML/CSS Conventions

**HTML:**
- Use semantic HTML5 elements (`<section>`, `<nav>`, `<article>`)
- Use German text throughout (educational content)
- Include emoji for visual appeal (e.g., 📐, 📖, 🎯)
- Proper indentation (2 or 4 spaces consistently)

**CSS:**
- Use class selectors over ID selectors where possible
- Mobile-first responsive design
- Use CSS variables for colors (if refactoring)
- Clear comments for major sections

### Consistent Terminology

**German Terms (Use These):**
- Zuordnung = Assignment/Mapping
- Proportional = Proportional
- Antiproportional = Antiproportional (or inverse proportion)
- Übung = Exercise
- Quiz = Quiz
- Theorie = Theory
- Fortschritt = Progress
- Level = Level
- Dreisatz = Rule of three

## Important Considerations for AI Assistants

### 1. Version Synchronization

**CRITICAL**: When adding features or fixing bugs, consider whether changes should be applied to all three versions:

- **UI changes**: Usually need to be replicated across all versions
- **Exercise content**: Should be identical in all versions
- **Quiz questions**: Should be identical in all versions
- **Bug fixes**: Check if the bug exists in other versions
- **New features**: Discuss with user whether to implement in all versions

### 2. German Language

All user-facing text is in German. When making changes:
- Maintain German language for all UI text
- Use proper German grammar and spelling
- Keep emoji usage consistent with existing patterns
- Error messages should be in German
- Code comments can be in German or English

### 3. Educational Focus

This is an educational application for 7th graders:
- Keep language simple and clear
- Provide detailed explanations for answers
- Maintain encouraging, positive tone
- Avoid overly technical terminology
- Real-world examples are important

### 4. No External Dependencies (Standalone)

The standalone version (`index.html` + `app.js`) has ZERO dependencies:
- No jQuery, React, Vue, etc.
- No npm, webpack, or build process
- Pure vanilla JavaScript
- Must work offline
- Don't add any external libraries without explicit permission

### 5. Progress Persistence

Each version handles persistence differently:
- **Standalone**: LocalStorage (persists across sessions)
- **Flask**: Server-side sessions (persists during session only)
- **Desktop**: In-memory (lost on close)

Be aware of these differences when debugging or adding features.

### 6. Mathematical Accuracy

The app teaches real mathematics:
- Ensure all calculations are correct
- Verify formulas: proportional (y₁/x₁ = y₂/x₂), antiproportional (x₁·y₁ = x₂·y₂)
- Test edge cases (division by zero, very large numbers, decimals)
- Round appropriately for display (usually 2 decimal places)

### 7. Error Handling Best Practices

The `math_utils.py` module demonstrates professional error handling:
- Always validate inputs before processing
- Use custom exception types for different error categories
- Provide clear, actionable error messages
- Handle edge cases explicitly
- Document expected exceptions in docstrings

### 8. File Modifications

**When modifying files:**
- Use the Edit tool for existing files (preferred)
- Only use Write for new files
- Read files before editing them
- Preserve exact indentation and formatting
- Don't add features beyond what's requested

**Key files to be careful with:**
- `app.js` (680 lines) - Complex state management
- `zuordnungen_app.py` (1242 lines) - Large tkinter application
- `web_app.py` (384 lines) - Flask routes and logic

### 9. Testing Checklist

Before marking changes complete, verify:
- [ ] All three versions updated (if applicable)
- [ ] No syntax errors in code
- [ ] Mathematical calculations are correct
- [ ] German language is grammatically correct
- [ ] Progress tracking still works
- [ ] Adaptive difficulty still functions
- [ ] No console errors (for web versions)
- [ ] Responsive design still works
- [ ] LocalStorage/session handling unchanged

### 10. Documentation Updates

When adding features, update relevant README files:
- `README.md` - If it affects all versions
- `README_STANDALONE.md` - For standalone version changes
- `README_WEB.md` - For Flask version changes
- `README_APP.md` - For desktop version changes

### 11. Common Pitfall: Duplicate Logic

Exercise generation, quiz logic, and theory content exist in **three separate files**. When you find a bug:

```
Bug in app.js → Also check web_app.py AND zuordnungen_app.py
```

Don't just fix it in one place!

## Common Tasks Reference

### Add a New Theory Section

1. **HTML** (`index.html` ~line 60-120):
   ```html
   <div class="tab-content" id="tab5">
       <h3>New Section Title</h3>
       <p>Content here...</p>
   </div>
   ```

2. **JavaScript** (`app.js` ~line 30):
   ```javascript
   <button class="tab-button" onclick="openTab('tab5')">📚 New Section</button>
   ```

3. **Flask template** (`templates/theorie.html`):
   Add corresponding section

4. **Desktop GUI** (`zuordnungen_app.py` ~line 250):
   Add new tab to notebook widget

### Modify Difficulty Thresholds

Look for these locations:
- `app.js:520` - `if (accuracy > 0.7 && this.progress.total_attempts >= 5)`
- `web_app.py:340` - Similar logic in Flask
- `zuordnungen_app.py:850` - Similar logic in tkinter

### Add Progress Metrics

1. Add to progress object initialization in all versions
2. Update progress display logic
3. Update progress page/screen rendering
4. Ensure persistence works correctly

### Fix Mathematical Errors

1. Locate the exercise generation function
2. Find the specific level template
3. Verify formula and calculation
4. Test with multiple inputs
5. Update in all three versions

## Deployment Notes

### Standalone Version (Production-Ready)

**Deployment is trivial:**
```bash
# Copy these files to any web server:
index.html
app.js
static/css/style.css
static/js/main.js
```

**Or serve locally:**
```bash
python3 -m http.server 8000
# Visit: http://localhost:8000
```

**No build process needed!**

### Flask Web Version

**Local Development:**
```bash
pip install flask
python3 START.py
```

**Production Deployment** (if needed):
- Use production WSGI server (gunicorn, uWSGI)
- Change `app.secret_key` to random secure value
- Set `app.debug = False`
- Consider using Redis for session storage
- Example with gunicorn:
  ```bash
  pip install gunicorn
  gunicorn -w 4 -b 0.0.0.0:5000 web_app:app
  ```

### Desktop GUI Version

**Distribution:**
- Users need Python 3.6+ with tkinter
- Provide platform-specific launcher scripts
- Consider PyInstaller for standalone executables:
  ```bash
  pip install pyinstaller
  pyinstaller --onefile --windowed zuordnungen_app.py
  ```

## Project Statistics

- **Total Size**: ~609 KB
- **Total Lines of Code**: ~5,969
- **Languages**: Python (3 files), JavaScript (2 files), HTML (7 files), CSS (1 file)
- **Documentation**: 5 README files
- **Supported Platforms**: Web browsers, Windows, macOS, Linux

## Contact & Support

For questions or issues:
- Create an issue in the repository
- Reference relevant files with line numbers
- Provide steps to reproduce (if bug)
- Specify which version (Standalone/Flask/Desktop)

## Version History

- **Latest**: Added standalone HTML/JS version as recommended option
- **Previous**: Flask web version and desktop GUI version
- **Initial**: Desktop tkinter application only

---

**Last Updated**: 2026-01-13
**Maintained By**: AI Assistant Claude
**Project Language**: German (Deutsch)
**Target Audience**: 7th Grade Mathematics Students (Klasse 7)
