// Jest test for React component
test('renders AXIOMHIVE header', () => {
  const { getByText } = render(<App />);
  expect(getByText('AXIOMHIVE Dominion')).toBeInTheDocument();
});
