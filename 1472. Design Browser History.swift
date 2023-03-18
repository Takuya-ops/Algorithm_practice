class BrowserHistory {
    private var history: [String], future: [String]
    private var current: String

    init(_ homepage: String) {
        history = [String]()
        future = [String]()
        current = homepage
    }
    
    func visit(_ url: String) {
        history.append(current)
        current = url
        future = [String]()
    }
    
    func back(_ steps: Int) -> String {
        for _ in 0..<steps {
            guard !history.isEmpty else { break }
            future.append(current)
            current = history.removeLast()
        }
        return current
    }
    
    func forward(_ steps: Int) -> String {
        for _ in 0..<steps {
            guard !future.isEmpty else { break }
            history.append(current)
            current = future.removeLast()
        }
        return current
    }
}