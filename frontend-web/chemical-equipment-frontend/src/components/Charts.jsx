function Charts({ distribution }) {
  if (!distribution || typeof distribution !== "object") return null;

  return (
    <div style={{ marginTop: "30px" }}>
      <h3>Equipment Type Distribution</h3>
      <ul>
        {Object.entries(distribution).map(([type, count]) => (
          <li key={type}>
            {type}: {count}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Charts;