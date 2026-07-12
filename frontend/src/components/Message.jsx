import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { oneDark } from "react-syntax-highlighter/dist/esm/styles/prism";

function Message({ message }) {
  return (
    <div
      className={
        message.role === "user"
          ? "message user-message"
          : "message bot-message"
      }
    >
      <strong>
        {message.role === "user" ? "You" : "IntentOS"}
      </strong>

      {message.loading && message.content === "" ? (
    <div className="thinking">
        <span></span>
        <span></span>
        <span></span>
    </div>
) : (
    <ReactMarkdown
      remarkPlugins={[remarkGfm]}
      components={{
        code({ inline, className, children, ...props }) {
          const match = /language-(\w+)/.exec(className || "");

          return !inline && match ? (
            <SyntaxHighlighter
              style={oneDark}
              language={match[1]}
              PreTag="div"
              {...props}
            >
              {String(children).replace(/\n$/, "")}
            </SyntaxHighlighter>
          ) : (
            <code className={className} {...props}>
              {children}
            </code>
          );
        },
      }}
    >
      {message.content}
    </ReactMarkdown>
)}
    </div>
  );
}

export default Message;