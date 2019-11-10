#!/usr/bin/perl

use strict;
use warnings;

our $true = 1;
our $false = 0;


=item print_string(string)
Prints string with a newline
=cut
sub print_string
{
	print "$_[0]\n";
}


=item take_multiple_args(A, B, C, D)
Prints each argument on a separate line
=cut
sub take_multiple_args
{
	for my $item (@_)
	{
		print("$item\n");
	}
}


=item split_string(string)
Splits a string by comma
=cut
sub split_string
{
	my @str = split ",", $_[0];
	for my $s (@str)
	{
		print "$s\n";
	}
}


=item pattern_match(string, pattern)
Returns true if a pattern is in a stgring, else false
=cut
sub pattern_match
{
	my $string = $_[0];
	my $pattern = $_[1];
	if (! $string || ! $pattern)
	{
		print "Need to provide a string and pattern, respectively\n";
		return;
	}
	if ($string =~ /$pattern/)
	{
		print "True\n";
		return $true;
	}
	return $false;
}


=item bash_command_ls
Shows using a bash command through perl and capturing the output
=cut
sub bash_command_ls
{
	my $ls = `ls`;
	print($ls);
}


=item hashes
Show examples of using hashes
=cut
sub hashes
{
	my %simple;
	$simple{1} = "A";
	my %complex = (
		1 => "A",
		2 => "B",
		3 => "C",
	);
}


=item read_file_as_string
Reads an entire file as a string
=cut
sub read_file_as_string
{
	my $fname = $_[0];
	open my $F, '<', $fname or die "Read of $fname failed\n";
	my $fstring = do { local $/; <$F> };
	$fstring = strip_whitespace($fstring);
	return $fstring;
}


=item strip_whitespace
Strips whitespace on a string
=cut
sub string_whitespace
{
	my $string = $_[0];
	$string =~ s/^\s+|\s+$//g;
	return $string;
}


$true;
