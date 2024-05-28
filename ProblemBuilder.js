class ProblemBuilder {
    constructor(title, difficulty, description) {
        this.title = title;
        this.difficulty = difficulty;
        this.description = description;
        this.solution = null;
    }

    setSolution(solution) {
        this.solution = solution;
        return this;
    }
}