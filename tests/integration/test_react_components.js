// Jest test for React components
test('renders Betti visualization', () => {
  const { getByText } = render(<BettiViz />);
  expect(getByText('Betti Numbers')).toBeInTheDocument();
});
